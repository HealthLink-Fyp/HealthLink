import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/services/shared.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {

  amWho !:string;


  onSubmitWho(){
    if(this.amWho=='doctor'){
          this.shareService.amDoctor=true;
          this.router.navigate(['/doctor']);
    }
     else
     {
      this.shareService.amPatient=true;
      this.router.navigate(['/patient']);
     }

  
     console.log(this.shareService.amDoctor);
     console.log(this.shareService.amPatient);
    
  }



  message='';

  constructor(private authService:AuthService,private shareService:SharedService,private router:Router){}

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
