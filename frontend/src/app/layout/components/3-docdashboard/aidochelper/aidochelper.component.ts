import { Component } from '@angular/core';
import { take } from 'rxjs/operators';
import { SharedService } from 'src/app/architecture/services/shared.service';

@Component({
  selector: 'app-aidochelper',
  templateUrl: './aidochelper.component.html',
  styleUrls: ['./aidochelper.component.css']
})
export class AidochelperComponent {

  response: any;

  constructor(private sharedService: SharedService) { }

  ngOnInit(): void {
    this.sharedService.onResponseAvailable().pipe(take(1)).subscribe((data) => {
      this.response = data;
      console.log("the ai answer is coming in aidochelp", this.response);
    });
  }
}
