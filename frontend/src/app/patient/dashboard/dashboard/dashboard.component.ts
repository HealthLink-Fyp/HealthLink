import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';
import { PatientService } from 'src/app/services/patient/patient.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  patientData: any = {};



ngOnInit(): void {
  this.patientService.getPatient().subscribe((res:any)=>{
    this.patientData=res;
    console.log("coming from dashboard",this.patientData);
  }
    
  )
}

  constructor(private patientService:PatientService, private router:Router,private authService:AuthService){}

  searchQuery:string='';
  searchResults:any[]=[];
  selectedCity:string='';

  appointmentData: any = {
    start:'',
    doctor:'',
    patient:''
  };



   cities:string[]=[
   'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Hyderabad', 'Quetta', 'Peshawar', 'Gujranwala', 'Sialkot', 'Abbottabad', 'Bahawalpur', 'Sargodha', 'Sukkur', 'Larkana', 'Nawabshah', 'Mirpur Khas', 'Rahim Yar Khan', 'Sahiwal', 'Okara', 'Wah Cantonment', 'Dera Ghazi Khan', 'Mingora', 'Kamoke', 'Shekhupura', 'Mardan', 'Kasur', 'Gujrat', 'Chiniot', 'Jhang', 'Sadiqabad', 'Sheikhupura', 'Attock', 'Jhelum', 'Jacobabad', 'Khanewal', 'Muzaffargarh', 'Khanpur'
   ]

   afterSearchData:any[]=[];

  searchDoctors()
  {
    if(this.searchQuery===''){
      this.clearSearchResults();
      return
    }

   this.patientService.searchDoctors(this.searchQuery).subscribe(
      (response:any)=>{
          this.searchResults=response
          console.log(this.searchResults)
      },
    )
    }

    clearSearchResults()
    {
      this.searchResults=[];
    }

    doctorsSearched()
    {
      this.patientService.afterDoctorsSearched(this.searchQuery,this.selectedCity).subscribe((response:any)=>{
           this.afterSearchData=response.results;
           console.log('data came after search is : ',this.afterSearchData);
      })
    }

    viewDoctor(userId:any)
    {
      this.router.navigate(['/dboard',userId]);
        
    }

   
    onAppointment(docId:any)
    {
      this.authService.user().subscribe((res:any)=>{
        this.appointmentData.patient=res.id;
        console.log("the patient id is : ",res.id)
  
      
      
      this.appointmentData.doctor=docId;

      this.patientService.makeAppointment(this.appointmentData).subscribe((response:any)=>{
        console.log(response);
      })
    });
    }

    

}
