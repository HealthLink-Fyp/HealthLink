import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {

 
  constructor(private http: HttpClient) { }





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
    if (this.responseAvailable) {
      return this.responseAvailable;
    } else {
      return new EventEmitter<any>();
    }
  }
}
