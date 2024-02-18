import { PostsService } from "./client";

const response = await PostsService.createPostPostsPost({
  requestBody: { content: "this is a new post!", title: "new post" },
});

response.title;
