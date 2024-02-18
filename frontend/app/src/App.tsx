import "./App.css";
import { OpenAPI, PostsService } from "./client";

OpenAPI.BASE = "http://127.0.0.1:8000";

const posts = await PostsService.getAllPosts();

function App() {
  return <>{posts}</>;
}

export default App;
