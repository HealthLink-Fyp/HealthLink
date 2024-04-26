import { TestBed } from '@angular/core/testing';

import { TranscribeService } from './transcribe.service';

describe('TranscribeService', () => {
  let service: TranscribeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TranscribeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
