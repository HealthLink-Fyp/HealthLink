import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DtabsComponent } from './dtabs.component';

describe('DtabsComponent', () => {
  let component: DtabsComponent;
  let fixture: ComponentFixture<DtabsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DtabsComponent]
    });
    fixture = TestBed.createComponent(DtabsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
