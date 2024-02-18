import { createRoot } from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import PostCreate from "./pages/PostCreate";
import PostList from "./pages/PostList";

const router = createBrowserRouter([
  {
    path: "/",
    element: <PostList />,
  },
  {
    path: "create-post",
    element: <PostCreate />,
  },
]);

const rootElement = document.getElementById("root");

if (rootElement) {
  createRoot(rootElement).render(<RouterProvider router={router} />);
} else {
  console.error("Failed to find the root element");
}
