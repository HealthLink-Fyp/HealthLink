import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LayoutRoutingModule } from './layout-routing.module';
import { LayoutComponent } from './layout.component';

import {MatCardModule} from '@angular/material/card';
import { MaterialModule } from 'src/app/material/material/material.module';
import { Lay1Component } from './lay1/lay1.component';
import { FooterComponent } from '../footer/footer.component';
import { FooterModule } from '../footer/footer.module';
import { RouterModule } from '@angular/router';
import { LandingComponent } from '../topnav/landing.component';
import { LandingModule } from '../topnav/landing.module';
import { SearchbarModule } from '../searchbar/searchbar.module';
import { Card1Component } from '../cards/card1/card1.component';
import { CardsModule } from '../cards/cards.module';
import { SwipeModule } from '../swipe/swipe.module';

@NgModule({
  declarations: [
    LayoutComponent,
    Lay1Component,
    
  ],
  imports: [
    CommonModule,
    RouterModule,
    LayoutRoutingModule,
    MaterialModule,
    FooterModule,
    LandingModule,
    SearchbarModule,
    CardsModule,
    SwipeModule
  ]
})
export class LayoutModule { }
