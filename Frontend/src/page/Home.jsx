import { useEffect, useState } from "react";
import API from "../services/api";

function Home() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("test/")
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      {/* <h1>Data from Backend</h1>
      {data.map((item) => (
        <p key={item.id}>{item.name}</p>
      ))} */}
   <h1>   {data.message}</h1>
    </div>
  );
}

export default Home;