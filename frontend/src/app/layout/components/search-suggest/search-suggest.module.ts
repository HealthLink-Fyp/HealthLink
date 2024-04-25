import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SearchSuggestRoutingModule } from './search-suggest-routing.module';
import { SearchSuggestComponent } from './search-suggest.component';

import {MatIconModule} from '@angular/material/icon';

import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from 'src/app/material/material/material.module';


@NgModule({
  declarations: [
    SearchSuggestComponent
  ],
  imports: [
    CommonModule,
    SearchSuggestRoutingModule,
   
    MaterialModule
  ]
})
export class SearchSuggestModule { }
