import { environment } from './../../environment/environment';
import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  static authEmitter=new EventEmitter<boolean>();

  accessToken='';

  constructor(private http:HttpClient) { }

  register(body:any)
  {
    return this.http.post(`${environment.api}/register`,body);
  }

  login(body:any)
  {
    return this.http.post(`${environment.api}/login`,body,{withCredentials:true});
  }

  user()
  {
    return this.http.get(`${environment.api}/register`);
  }

  refresh()
  {
    return this.http.post(`${environment.api}/refresh`,{},{withCredentials:true});
  }

  logout()
  {
    return this.http.post(`${environment.api}/logout`,{},{withCredentials:true});
  }
}
