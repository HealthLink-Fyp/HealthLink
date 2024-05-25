import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {

 
  constructor(private http: HttpClient) { }

  
  
 



  private responseEm: any;
  private responseEmoteAvailable = new EventEmitter<any>();

  setEmoteData(data: any) {
    this.responseEm= data;
    this.responseEmoteAvailable.emit(data);
  }

  getResponseEmoteData(): any {
    return this.responseEm;
  }

  onResponseEmoteAvailable(): EventEmitter<any> {
    return this.responseEmoteAvailable;
  }



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
