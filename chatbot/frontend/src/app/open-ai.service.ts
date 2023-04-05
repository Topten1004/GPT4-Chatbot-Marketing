import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class OpenAIService {
  constructor(private http: HttpClient) {}

  getData(input: string): Observable<any> {
    return this.http.get(
      'https://localhost:7288/api/OpenAI/GetData?input=' + input,
      { responseType: 'text' }
    );
  }
}
