import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';
import { SharedService } from '../shared.service';

declare var webkitSpeechRecognition: any;

@Injectable({
  providedIn: 'root'
})
export class TranscribeService {

  recognition = new webkitSpeechRecognition();
  public doctorText = '';
  public patientText = '';
  tempWords: string | undefined;
  public isDoctor!: boolean;

  constructor(private http: HttpClient, private sharedService: SharedService) {}

  init() {
    this.recognition.interimResults = true;
    this.recognition.lang = 'en-US';

    this.recognition.addEventListener('result', (e: any) => {
      const transcript = Array.from(e.results)
        .map((result: any) => result[0].transcript)
        .join('');
      this.tempWords = transcript;
    });
  }

  start(isDoctor: boolean) {
    this.isDoctor = isDoctor; // Set whether the caller is a doctor or patient
    this.recognition.start();
    console.log("Speech recognition started");

    this.recognition.addEventListener('end', () => {
      this.wordConcat();
      this.recognition.start(); // Restart the recognition
    });
  }

  wordConcat() {
    if (this.tempWords) {
      if (this.isDoctor) {
        this.doctorText += ' ' + this.tempWords + '.';
      } else {
        this.patientText += ' ' + this.tempWords + '.';
      }
      console.log(this.tempWords);
      this.tempWords = '';
      this.sendTextToBackend();
    }
  }

  data = {
    transcription: '',
    patient_id: '',
    call_id: ''
  };

  sendTextToBackend() {
    const combinedText = this.doctorText + ' ' + this.patientText;

    if (combinedText.split(' ').length >= 100) {
      this.data.transcription = combinedText;
      this.http.post(`${environment.api}/calls/transcript/`, this.data).subscribe((res: any) => {
        console.log("The data before sending is here:", this.data);
        console.log("The text is successfully sent to backend", res);
        this.sharedService.setResponseData(res);
      });
      console.log("Sending text to backend API:", combinedText);
      console.log("patient bola ha : ",this.doctorText);
      console.log("doctor bola ha : ",this.patientText);
      this.doctorText = '';
      this.patientText = '';
    }
  }
}
