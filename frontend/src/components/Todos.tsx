import React, { useEffect, useState } from "react";

interface ToDoInterface {
  id: number;
  item: string;
}

interface TodoInterfaceContext {
  todos: ToDoInterface[];
}
interface TodosInterface {
  todos: ToDoInterface[];
}
const TodosContext = React.createContext<TodoInterfaceContext>({
  todos: [{ id: 0, item: "" }],
});

export default function Todos() {
  const [todos, setTodos] = useState<ToDoInterface[]>([{ id: 0, item: "" }]);
  const fetchTodos = async () => {
    const response = await fetch("http://localhost:8000/todo");
    const todos = await response.json();

    setTodos(todos);
  };
  useEffect(() => {
    fetchTodos();
  }, []);
  return (
    <TodosContext.Provider value={{ todos }}>
      <div>
        {todos.map((todoMap) => (
          <b>{todoMap.item}</b>
        ))}
      </div>
    </TodosContext.Provider>
  );
}
