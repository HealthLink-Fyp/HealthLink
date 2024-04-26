import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import {Peer, PeerError} from 'peerjs';
import { BehaviorSubject, Subject } from 'rxjs';
import { v4 as uuidv4 } from 'uuid';
import { MediaConnection } from 'peerjs';
import { PeerJSOption } from 'peerjs';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CallService {
  private peer: Peer | null = null;
  private mediaCall:MediaConnection |  undefined;

  private localStreamBs: BehaviorSubject<MediaStream> = new BehaviorSubject(new MediaStream());
  public localStream$ = this.localStreamBs.asObservable();

  private remoteStreamBs: BehaviorSubject<MediaStream> = new BehaviorSubject(new MediaStream());
  public remoteStream$ = this.remoteStreamBs.asObservable();

  private isCallStartedBs = new Subject<boolean>();
  public isCallStarted$ = this.isCallStartedBs.asObservable();

  constructor(private snackBar: MatSnackBar, private http:HttpClient) { }

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

  public async establishMediaCall(remotePeerId: string) {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

      const connection = this.peer?.connect(remotePeerId);
      connection?.on('error', (error: PeerError<"not-open-yet" | "message-too-big" | "negotiation-failed" | "connection-closed">)=>{
        console.error(error);
        this.snackBar.open(error.message, 'Close');
      });

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

  public async enableCallAnswer() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      this.localStreamBs.next(stream);
      this.peer?.on('call', async (call) => {
        this.mediaCall = call;
        this.isCallStartedBs.next(true);

        this.mediaCall.answer(stream);
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

  public closeMediaCall() {
    this.mediaCall?.close();
    if (!this.mediaCall) {
      this.onCallClose()
    }
    this.isCallStartedBs.next(false);
  }

  public destroyPeer() {
    this.mediaCall?.close();
    this.peer?.disconnect();
    this.peer?.destroy();
  }

  peerIdSend(peerId:any)
  {
    return this.http.post("www.xxx.com",peerId);
  }

  peerIdGet()
  {
    return this.http.get("www.xxx.com");
  }

}