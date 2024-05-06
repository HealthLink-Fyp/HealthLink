import { Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Observable, of } from 'rxjs';
import { filter, switchMap, take } from 'rxjs/operators';
import { CallService } from 'src/app/architecture/services/call/call.service';
import { DialogComponent,DialogData } from './dialog/dialog.component';
import { ActivatedRoute } from '@angular/router';
import { TranscribeService } from 'src/app/architecture/services/call/transcribe.service';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { SharedService } from 'src/app/architecture/services/shared.service';

@Component({
  selector: 'app-videocall',
  templateUrl: './videocall.component.html',
  styleUrls: ['./videocall.component.css']
})
export class VideocallComponent implements OnInit, OnDestroy {
  public isCallStarted$: Observable<boolean>;
  public peerId: string; 

  @ViewChild('localVideo') localVideo: ElementRef<HTMLVideoElement> | null = null;
  @ViewChild('remoteVideo') remoteVideo: ElementRef<HTMLVideoElement> | null=null;

  currentUserRole: string='';

  getCurrentUserRole() {
    this.authService.user().subscribe((user: any) => {
      this.currentUserRole = user.role;
    });
  }


  videoData: any = {
    peer_id:'',
    doctor:'',
    patient:'',
  };


  constructor(public dialog: MatDialog, private callService: CallService, private route:ActivatedRoute, private transcribeService:TranscribeService, private authService:AuthService, private sharedService:SharedService) {

    this.getCurrentUserRole();
    
    this.isCallStarted$ = this.callService.isCallStarted$;
    this.peerId = this.callService.initPeer();
    
    console.log("real peer id is ",this.peerId)
    //peeridsending to django backend for storage
    this.videoData.peer_id=this.peerId;

    this.videoData.patient=this.route.snapshot.paramMap.get('patientId');

    this.videoData.doctor=this.route.snapshot.paramMap.get('doctorId');

    console.log("information to unlock sending peer id in vid ts : ",this.videoData);

    this.callService.peerIdSend(this.videoData).subscribe((response:any)=>{
         console.log("the peer id have been sent vid ts.",response)
         this.sendCallIdToTranscribeService(response.call_id,response.patient);
    })
    
  }

  sendCallIdToTranscribeService(callId: any,patientId:any) {
    this.transcribeService.data.call_id = callId;
    this.transcribeService.data.patient_id=patientId;
  }

  transResponse: any='';

  fakeData = {
    "key_points": [
        "Patient's name: Tripura Amanda Flores",
        "Patient reluctant to share their name",
        "Location unknown"
    ],
    "likely_diagnoses": [
      "Alzehemier 50%",
      "Headache 40%",
      "Hiv 30%"
    ],
    "followup_questions": [
        "Can you provide your date of birth?",
        "Are you experiencing any specific symptoms or health concerns?",
        "Do you have any medical conditions or take any medications regularly?",
        "Can you describe your current location or any recent travel history?"
    ]
  };
  
  ngOnInit(): void {

    this.sharedService.onResponseAvailable().subscribe((data) => {
      this.transResponse='';
      this.transResponse = data;
      console.log("the ai answer is coming in aidochelp", this.transResponse);
    });

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
