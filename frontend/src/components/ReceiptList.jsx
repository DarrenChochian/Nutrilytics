import React, { useEffect, useState } from "react";
import axios from "axios";

function ReceiptList({ userId }) {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get(`/api/get-groceries?user_id=${userId}`)
      .then(res => setItems(res.data))
      .catch(err => console.error(err));
  }, [userId]);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">Your Groceries</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name} - ${item.price.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReceiptList;
