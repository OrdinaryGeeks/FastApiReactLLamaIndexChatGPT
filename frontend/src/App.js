import "./App.css";
import Header from "./components/Header.tsx";
import Todos from "./components/Todos.tsx";
import HireNathan from "./components/HireNathan.tsx";
function App() {
  return (
    <div className="App">
      <Header />
      <Todos />
      <HireNathan />
    </div>
  );
}

export default App;
