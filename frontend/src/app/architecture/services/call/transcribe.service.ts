import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';

declare var webkitSpeechRecognition: any;

@Injectable({
  providedIn: 'root'
})
export class TranscribeService {

  recognition =  new webkitSpeechRecognition();
  public text = '';
  tempWords: string | undefined;

  constructor(private http:HttpClient) { }

  init() {

    this.recognition.interimResults = true;
    this.recognition.lang = 'en-US';

    this.recognition.addEventListener('result', (e: any) => {
      const transcript = Array.from(e.results)
        .map((result: any) => result[0].transcript)
        .join('');
      this.tempWords = transcript;
      // console.log(transcript);
    });
  }

  start() {
    this.recognition.start();
    console.log("Speech recognition started");

    this.recognition.addEventListener('end', (condition: any) => {
      this.wordConcat()
      
      this.recognition.start(); // Restart the recognition
    }
    );
  }

  wordConcat() {
    if (this.tempWords) {
      this.text = this.text + ' ' + this.tempWords + '.';
      console.log(this.tempWords);
      this.tempWords = '';
      this.sendTextToBackend();
    }

  }

  sendTextToBackend() {
    if (this.text.split(' ').length >= 150) {
      const data = {
        transcription: this.text,
        patient_id: 2,
        call_id: 6
      };
      this.http.post(`${environment.api}/calls/transcript/`, data).subscribe((res: any) => {
        console.log("The text is successfully sent to backend", res)
      })
      console.log("Sending text to backend API:", this.text);
      this.text = ''; // Reset the 'text' variable after sending to the API
    }
  }
  }
   
