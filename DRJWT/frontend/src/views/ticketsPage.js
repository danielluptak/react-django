import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";

function App() {
  const [tickets, setTickets] = useState([]);
  const api = useAxios();

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const { data } = await api.get("tickets/");
        const tickets = data;
        setTickets(tickets);
        console.log(tickets);
      } catch {
        setTickets("Something went wrong");
      }
    };

    fetchTickets();
  }, []);

  return (
    <div>
      {tickets.map((ticket) => (
        <p key={ticket.id}>{ticket.title}</p>
      ))}
    </div>
  );
}

export default App;

