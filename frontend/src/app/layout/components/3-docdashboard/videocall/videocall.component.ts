import { Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Observable, of } from 'rxjs';
import { filter, switchMap } from 'rxjs/operators';
import { CallService } from 'src/app/architecture/services/call/call.service';
import { DialogComponent,DialogData } from './dialog/dialog.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-videocall',
  templateUrl: './videocall.component.html',
  styleUrls: ['./videocall.component.css']
})
export class VideocallComponent implements OnInit, OnDestroy {
  public isCallStarted$: Observable<boolean>;
  public peerId: string;

   patient=2;
  doctor=1;
  peer_id:string=""
  

  @ViewChild('localVideo') localVideo: ElementRef<HTMLVideoElement> | null = null;
  @ViewChild('remoteVideo') remoteVideo: ElementRef<HTMLVideoElement> | null=null;


  videoData: any = {
    peer_id:'',
    doctor:'',
    patient:'',
  };


  constructor(public dialog: MatDialog, private callService: CallService, private route:ActivatedRoute) {
    this.isCallStarted$ = this.callService.isCallStarted$;
    this.peerId = this.callService.initPeer();
    
    console.log("real peer id is ",this.peerId)
    //peeridsending to django backend for storage
    this.videoData.peer_id=this.peerId;

    this.videoData.patient=this.route.snapshot.paramMap.get('patientId');

    this.videoData.doctor=this.route.snapshot.paramMap.get('doctorId');

    console.log("the videoData contains : ",this.videoData);

    this.callService.peerIdSend(this.videoData).subscribe((response:any)=>{
         console.log("the peer id have been sent.",response)
    })
    
  }
  
  ngOnInit(): void {
    this.callService.localStream$
      .pipe(filter(res => !!res))
      .subscribe(stream => {
        if (this.localVideo) {
          this.localVideo.nativeElement.srcObject = stream;
        }
      })
    this.callService.remoteStream$
      .pipe(filter(res => !!res))
      .subscribe(stream => {
        if (this.remoteVideo) {
          this.remoteVideo.nativeElement.srcObject = stream;
        }
      })
  }
  
  ngOnDestroy(): void {
    this.callService.destroyPeer();
  }

  public showModal(joinCall: boolean): void {
    let dialogData: DialogData = joinCall ? ({ peerId: undefined, joinCall: true }) : ({ peerId: this.peerId, joinCall: false });
    const dialogRef = this.dialog.open(DialogComponent, {
      width: '250px',
      data: dialogData
    });

    dialogRef.afterClosed()
      .pipe(
        switchMap(peerId => 
          joinCall ? of(this.callService.establishMediaCall(peerId)) : of(this.callService.enableCallAnswer())
        ),
      )
      .subscribe(_  => { });
  }

  public endCall() {
    this.callService.closeMediaCall();
  }
}
