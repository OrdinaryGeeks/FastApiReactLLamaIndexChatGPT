import React, { useState } from "react";
import axios from "axios";

interface Question {
  question: string;
}
const hireNathanQuestion = (event) => {
  event.preventDefault();
  const hiringQuestion: Question = { question: event.target.question.value };
  alert(hiringQuestion.question);
  axios
    .post<Question>("http://localhost:8000/shouldwehireNathan", hiringQuestion)
    .then((response) => alert(response.data));
};
export default function HireNathan() {
  const [answer, setAnswer] = useState("");

  return (
    <div>
      <form onSubmit={hireNathanQuestion}>
        <input type="text" name="question"></input>
        <button type="submit">Hire Nathan</button>
      </form>
    </div>
  );
}
