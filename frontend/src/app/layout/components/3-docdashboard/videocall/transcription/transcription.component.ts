import { Component } from '@angular/core';
import { TranscribeService } from 'src/app/architecture/services/call/transcribe.service';

@Component({
  selector: 'app-transcription',
  templateUrl: './transcription.component.html',
  styleUrls: ['./transcription.component.css']
})
export class TranscriptionComponent {
  text!: string;

  constructor(
    public service : TranscribeService
  ) { 
    this.service.init()
   }

  ngOnInit(): void {
  }

  startService(){
    this.service.start()
  }

  stopService(){
    // this.service.stop()
  }

}
