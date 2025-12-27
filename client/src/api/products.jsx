import axios from "axios";

const product_list = "http://10.0.2.2:8000/";

const ProductList = async () => {
  const prod = await axios.get(`${product_list}products/`);
  return prod.data;
};

export default ProductList;