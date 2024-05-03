import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {
  
  constructor( private http: HttpClient) {}

  private keys = {
    patientId: '',
    doctorId: ''
  };

  getKeys(): Observable<any> {
    return of({ patientId: this.keys.patientId, doctorId: this.keys.doctorId });
  }

  updateKeys(patientId: string, doctorId: string) {
    this.keys.patientId = patientId;
    this.keys.doctorId = doctorId;
  }

}
