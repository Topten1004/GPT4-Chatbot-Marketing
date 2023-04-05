import { Component } from '@angular/core';
import { OpenAIService } from './open-ai.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'CoreGPT.UI';
  searchTxtVal: string = '';
  output: string = '';
  showOutput: boolean = false;
  isLoading: boolean = false;

  constructor(private service: OpenAIService) {}

  getResult() {
    this.isLoading = true;
    this.output = '';
    this.service.getData(this.searchTxtVal).subscribe((data) => {
      this.output = data as string;
      this.showOutput = true;
      this.isLoading = false;
    });
  }
}
