import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {
  
  private response: any;
  private responseAvailable = new EventEmitter<any>();

  constructor() { }

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
