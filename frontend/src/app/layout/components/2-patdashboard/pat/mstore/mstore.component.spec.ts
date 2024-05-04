import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MstoreComponent } from './mstore.component';

describe('MstoreComponent', () => {
  let component: MstoreComponent;
  let fixture: ComponentFixture<MstoreComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MstoreComponent]
    });
    fixture = TestBed.createComponent(MstoreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
