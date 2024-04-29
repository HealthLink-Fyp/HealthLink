import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PtabsComponent } from './ptabs.component';

describe('PtabsComponent', () => {
  let component: PtabsComponent;
  let fixture: ComponentFixture<PtabsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PtabsComponent]
    });
    fixture = TestBed.createComponent(PtabsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
