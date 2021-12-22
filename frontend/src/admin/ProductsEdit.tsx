import React, {
  PropsWithRef,
  SyntheticEvent,
  useEffect,
  useState,
} from "react";
import Wrapper from "./Wrapper";
import { Navigate, useParams } from "react-router-dom";
import { Product } from "../interfaces/product";

const ProductsEdit = (props: PropsWithRef<any>) => {
  const params = useParams();
  const id = params.id;
  const [title, setTitle] = useState("");
  const [image, setImage] = useState("");
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    (async () => {
      const response = await fetch(`http://localhost:8000/api/products/${id}`);

      const product: Product = await response.json();

      setTitle(product.title);
      setImage(product.image);
    })();
  }, []);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    await fetch(`http://localhost:8000/api/products/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        image,
      }),
    });

    setRedirect(true);
  };

  if (redirect) {
    return <Navigate to={"/admin/products"} />;
  }

  return (
    <Wrapper>
      <h3>Edit products</h3>
      <form onSubmit={submit}>
        <div className="form-group">
          <label>Title</label>
          <input
            type="text"
            className="form-control"
            name="title"
            defaultValue={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Image</label>
          <input
            type="text"
            className="form-control"
            name="image"
            defaultValue={image}
            onChange={(e) => setImage(e.target.value)}
          />
        </div>
        <button className="btn btn-outline-secondary">Save</button>
      </form>
    </Wrapper>
  );
};

export default ProductsEdit;
