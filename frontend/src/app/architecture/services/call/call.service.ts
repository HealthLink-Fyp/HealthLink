import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import {Peer, PeerError} from 'peerjs';
import { BehaviorSubject, Subject } from 'rxjs';
import { v4 as uuidv4 } from 'uuid';
import { MediaConnection } from 'peerjs';
import { PeerJSOption } from 'peerjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environment/environment';


@Injectable({
  providedIn: 'root'
})
export class CallService {
  private peer: Peer | null = null;

  // Alice initiates a media call to Bob, establishing a connection.

  private mediaCall:MediaConnection |  undefined;

  // Alice's device stores its media stream in localStreamBs and shares it with Bob via localStream$.

  private localStreamBs: BehaviorSubject<MediaStream> = new BehaviorSubject(new MediaStream());
  public localStream$ = this.localStreamBs.asObservable();

  // Bob's device stores Alice's media stream in remoteStreamBs and receives it via remoteStream$.

  private remoteStreamBs: BehaviorSubject<MediaStream> = new BehaviorSubject(new MediaStream());
  public remoteStream$ = this.remoteStreamBs.asObservable();

  // When the call starts, isCallStartedBs emits a boolean value, and isCallStarted$ notifies the application.
  
  private isCallStartedBs = new Subject<boolean>();
  public isCallStarted$ = this.isCallStartedBs.asObservable();

  constructor(private snackBar: MatSnackBar, private http:HttpClient) { }

  // generating a unique peer ID (e.g., "alice123")

  public initPeer(): string {
    if (!this.peer || this.peer.disconnected) {
      const peerJsOptions: PeerJSOption = {
        debug: 3,
        config: {
          iceServers: [
            {
              urls: [
                                'stun:stun1.l.google.com:19302',
                                'stun:stun2.l.google.com:19302',
              ],
            }]
        }
      };
      try {
        let id = uuidv4();
        this.peer = new Peer(id, peerJsOptions);
        return id;
      } catch (error) {
        console.error(error);
      }
      
    }
    return ""; 
  }

  // Alice wants to call Bob, so she clicks the "Call" button. The establishMediaCall() method is called, passing Bob's peer ID (e.g., "bob456").

  public async establishMediaCall(remotePeerId: string) {
    try {

      // Gets Alice's local media stream (video and audio) 

      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

      // Creates a new PeerJS connection to Bob's device using peer.connect().

      const connection = this.peer?.connect(remotePeerId);
      connection?.on('error', (error: PeerError<"not-open-yet" | "message-too-big" | "negotiation-failed" | "connection-closed">)=>{
        console.error(error);
        this.snackBar.open(error.message, 'Close');
      });

      // Calls Bob's device with Alice's local media stream using peer.call().

      this.mediaCall = this.peer?.call(remotePeerId, stream);
      if (!this.mediaCall) {
        let errorMessage = 'Unable to connect to remote peer';
        this.snackBar.open(errorMessage, 'Close');
        throw new Error(errorMessage);
      }
      this.localStreamBs.next(stream);
      this.isCallStartedBs.next(true);

      this.mediaCall.on('stream', (remoteStream: MediaStream) => {
        this.remoteStreamBs.next(remoteStream);
      });
      this.mediaCall.on('error', (error: PeerError<"negotiation-failed" | "connection-closed">) => {
        this.snackBar.open(error.message, 'Close');
        console.error(error);
        this.isCallStartedBs.next(false);
      });
      this.mediaCall.on('close', () => this.onCallClose());
    } catch (ex: unknown) {
      console.error(ex);
      this.snackBar.open('Error occurred', 'Close');
      this.isCallStartedBs.next(false);
    }
  }

  // When Bob receives the call, the enableCallAnswer() method is called.

  public async enableCallAnswer() {
    try {

      // Gets Bob's local media stream (video and audio) using navigator.mediaDevices.getUserMedia().

      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      this.localStreamBs.next(stream);
      this.peer?.on('call', async (call) => {
        this.mediaCall = call;
        this.isCallStartedBs.next(true);

        // Answers the call with Bob's local media stream using mediaCall.answer().

        this.mediaCall.answer(stream);

        // The mediaCall.on('stream', ...) event listener is triggered when Bob's media stream is received, and it updates the remote stream observable.
       
        this.mediaCall.on('stream', (remoteStream: MediaStream) => {
          this.remoteStreamBs.next(remoteStream);
        });
        this.mediaCall.on('error', (error: PeerError<"negotiation-failed" | "connection-closed">) => {
          this.snackBar.open(error.message, 'Close');
          console.error(error);
          this.isCallStartedBs.next(false);
        });
        this.mediaCall.on('close', () => this.onCallClose());
      });      
    } catch (ex: unknown) {
      console.error(ex);
      this.snackBar.open('Error occurred', 'Close');
      this.isCallStartedBs.next(false);
    }
  }

  private onCallClose() {
    this.remoteStreamBs?.value.getTracks().forEach(track => {
      track.stop();
    });
    this.localStreamBs?.value.getTracks().forEach(track => {
      track.stop();
    });
    this.snackBar.open('Call Ended', 'Close');
  }

  
  // When Alice or Bob ends the call, the closeMediaCall() method is called, which closes the media call and stops the media tracks.

  public closeMediaCall() {
    this.mediaCall?.close();
    if (!this.mediaCall) {
      this.onCallClose()
    }
    this.isCallStartedBs.next(false);
  }

  // When Alice closes the application, the destroyPeer() method is called, which destroys the PeerJS instance and releases resources.
 
  public destroyPeer() {
    this.mediaCall?.close();
    this.peer?.disconnect();
    this.peer?.destroy();
  }



  peerIdSend(videoData:any) {
   
    return this.http.post(`${environment.api}/calls/`, videoData);
  }

  peerIdGet()
  {
    return this.http.get(`${environment.api}/calls/`);
  }

}