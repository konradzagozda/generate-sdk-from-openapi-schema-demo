import { OpenAPI, PostsService } from "./client";

OpenAPI.BASE = "http://127.0.0.1:8000";

async function main() {
  const newPost = await PostsService.createPost({
    requestBody: { content: "content", title: "title", published: true },
  });

  console.log("created post", newPost);

  const allPosts = await PostsService.getAllPosts();

  console.log("all posts", allPosts);

  const latestPost = await PostsService.getLatestPost();

  console.log("latest post", latestPost);

  await PostsService.deletePost({ id: latestPost.id });

  const latestPostAfterDelete = await PostsService.getLatestPost();

  console.log("latestPostAfterDelete", latestPostAfterDelete);
}

main();
