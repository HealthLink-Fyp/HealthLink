import { Component } from '@angular/core';
import { PatientService } from 'src/app/services/patient/patient.service';

@Component({
  selector: 'app-docsearch',
  templateUrl: './docsearch.component.html',
  styleUrls: ['./docsearch.component.css']
})
export class DocsearchComponent {

  constructor(private patientService:PatientService){}


  searchQuery:string='';          // stores the words  that user types in search
  searchResults:any[]=[];          //stores the automcomplete searchResults of doctors
  selectedCity:string='';          //stores that city in which user wants to search doctor
  bookedAppointments:any[] = []; 

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
{                                          //if userpresses backspace and clear the search bar then remove the search results showing on the screen
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
      this.patientService.afterDoctorsSearched(this.searchQuery,this.selectedCity).subscribe((response:any)=>{
           this.afterSearchData=response.results;
           console.log('data came after search is : ',this.afterSearchData);
      })
    }
}
