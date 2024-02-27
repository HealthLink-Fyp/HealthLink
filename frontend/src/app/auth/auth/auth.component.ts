import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {



  message='';

  constructor(private authService:AuthService){}

  ngOnInit(): void {
    this.authService.user().subscribe({
      next:(res:any)=>{
         this.message=`Hi ${res.first_name} ${res.last_name}`;
         AuthService.authEmitter.emit(true);
      },
      error:err=>{
         this.message='u r not authenticated';
         AuthService.authEmitter.emit(false);
      }
    })
  }

}
