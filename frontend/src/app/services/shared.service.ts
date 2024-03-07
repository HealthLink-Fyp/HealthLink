import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  constructor(http:HttpClient) { }

    amDoctor=false;

    amPatient=false;

}
