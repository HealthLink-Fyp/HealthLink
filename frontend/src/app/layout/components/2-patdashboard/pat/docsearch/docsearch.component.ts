import { Component, NgZoneOptions, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { Location } from '@angular/common';
import { HttpClient } from '@angular/common/http';



@Component({
  selector: 'app-docsearch',
  templateUrl: './docsearch.component.html',
  styleUrls: ['./docsearch.component.css']
})
export class DocsearchComponent implements OnInit {


  currentUserRole: string='';

  getCurrentUserRole() {
    this.authService.user().subscribe((user: any) => {
      this.currentUserRole = user.role;
    });
  }



  constructor(private patientService:PatientService, private router:Router, private authService:AuthService, private location: Location,private http: HttpClient){
   
    this.getCurrentUserRole();
  
  }

  ngOnInit(): void {

    console.log("i am ngoniit");
  }

  
  

 






  // if the user who visiting this components have token in his headers then check the boolean value to true otherwise false
 




  goBack(): void {
    this.location.back();
  }


  searchQuery:string='';          // stores the words  that user types in search
  searchResults:any[]=[];          //stores the automcomplete searchResults of doctors
  selectedCity:string='';          //stores that city in which user wants to search doctor
  bookedAppointments:any[] = []; 

  onClickSearchBtnBool:boolean=true;

  appointmentData: any = {
    start:'',
    doctor:'',
    patient:''
  };

  cities:string[]=[
    'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Hyderabad', 'Quetta', 'Peshawar', 'Gujranwala', 'Sialkot', 'Abbottabad', 'Bahawalpur', 'Sargodha', 'Sukkur', 'Larkana', 'Nawabshah', 'Mirpur Khas', 'Rahim Yar Khan', 'Sahiwal', 'Okara', 'Wah Cantonment', 'Dera Ghazi Khan', 'Mingora', 'Kamoke', 'Shekhupura', 'Mardan', 'Kasur', 'Gujrat', 'Chiniot', 'Jhang', 'Sadiqabad', 'Sheikhupura', 'Attock', 'Jhelum', 'Jacobabad', 'Khanewal', 'Muzaffargarh', 'Khanpur'
    ]

  search()
  {
    
  }

  searchSuggestions: string[] = [
    "Dentist",
    "Gynecologist",
    "General Physician",
    "Dermatologist",
    "Ear-nose-throat Specialist",
    "Homoeopath",
    "Ayurveda"
];

searchDoctors()
{          
  this.onClickSearchBtnBool=true;                                
  //if userpresses backspace and clear the search bar then remove the search results showing on the screen
  if(this.searchQuery===''){
    this.clearSearchResults();
    return                                // after that don't go further and don't make any more calls
  }

 this.patientService.searchDoctors(this.searchQuery).subscribe(
    (response:any)=>{
        this.searchResults=response
        console.log(this.searchResults)
    },
  )
  }

  // for clearing auto complete search reuslts

  clearSearchResults()
  {
    this.searchResults=[];
  }

   //array that stores all results of doctor after clicking on search button

   afterSearchData:any[]=[];

  doctorsSearched()
    {
      this.onClickSearchBtnBool=false;

      this.patientService.afterDoctorsSearched(this.searchQuery,this.selectedCity).subscribe((response:any)=>{
           this.afterSearchData=response.results;
           console.log('data came after search is : ',this.afterSearchData);
      })
    }

  

   
    onBookAppointment(docId:any)
    {
     this.router.navigate(['/dashboard/patient/appointment/booking']);
    }
}
