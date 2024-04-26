import { environment } from './../../environment/environment';
import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  static authEmitter = new EventEmitter<boolean>();

  accessToken = '';

  constructor(private http: HttpClient) {}

  register(body: any) {
    return this.http.post(`${environment.api}/auth/register/`, body);
  }

  login(body: any) {
    return this.http.post(`${environment.api}/auth/login/`, body, {
      withCredentials: true,
    });
  }

  user() {
    return this.http.get(`${environment.api}/auth/user/`);
  }

  updateUser(body:any)
  {
    return this.http.put(`${environment.api}/auth/user/`,body);
  }

  refresh() {
    return this.http.post(
      `${environment.api}/auth/refresh/`,
      {},
      { withCredentials: true },
    );
  }

  logout() {
    return this.http.post(
      `${environment.api}/auth/logout/`,
      {},
      { withCredentials: true },
    );
  }
}
