import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {

  transcriptionData:any = {
    doctor: '',
    patient: ''
  };
  backendUrl = 'https://your-django-backend.com/transcription-endpoint'; // replace with your actual endpoint URL

  constructor(private http: HttpClient) { }

  updateDoctorTranscription(data:any) {
    this.transcriptionData.doctor = data;
  }

  updatePatientTranscription(data:any) {
    this.transcriptionData.patient = data;
  }

  sendDataToBackend() {
    const data = {
      transcription: this.transcriptionData.doctor + ' ' + this.transcriptionData.patient
    };

    if (data.transcription.length >= 100) {
            this.http.post(this.backendUrl, data)
        .subscribe(response => {
          console.log('Data sent to backend successfully!');
        }, error => {
          console.error('Error sending data to backend:', error);
        });
    }
  }






    // this.http.post(this.backendUrl, data)
    //   .subscribe(response => {
    //     console.log('Data sent to backend successfully!');
    //   }, error => {
    //     console.error('Error sending data to backend:', error);
    //   });


      // sendTextToBackend() {
      //   if (this.text.split(' ').length >= 50) {
      //     this.data.transcription=this.text;
      //     this.http.post(`${environment.api}/calls/transcript/`, this.data).subscribe((res: any) => {
      //       console.log("The data before sending is here : ",this.data)
      //       console.log("The text is successfully sent to backend", res)
      //       this.sharedService.setResponseData(res);
      //     })
      //     console.log("Sending text to backend API:", this.text);
      //     this.text = ''; // Reset the 'text' variable after sending to the API
      //   }
      // }
  








  
  private response: any;
  private responseAvailable = new EventEmitter<any>();



  setResponseData(data: any) {
    this.response = data;
    this.responseAvailable.emit(data);
  }

  getResponseData(): any {
    return this.response;
  }

  onResponseAvailable(): EventEmitter<any> {
    return this.responseAvailable;
  }
}
