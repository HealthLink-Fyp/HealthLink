import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
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

  constructor(private patientService:PatientService){}

  searchQuery:string='';
  searchResults:any[]=[];
  selectedCity:string='';

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

   

    

}
