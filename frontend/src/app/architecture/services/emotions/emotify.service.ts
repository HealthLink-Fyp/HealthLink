import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';

@Injectable({
  providedIn: 'root'
})
export class EmotifyService {

  constructor(private http:HttpClient) { }


  sendImage(formData: FormData)
  {
    console.log("image sended ot backend",formData)
    return this.http.post(`${environment.api}/calls/emotion/`, formData).subscribe((response:any)=>{
console.log(response);
    });
  }
}
