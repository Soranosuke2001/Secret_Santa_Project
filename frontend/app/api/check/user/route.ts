import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  try {
    const username = request.nextUrl.searchParams.get("username");

    const response = await fetch(
      `${process.env.BACKEND_CHECK_USERNAME}?username=${username}`
    );

    if (!response.ok) {
      return new Response(JSON.stringify({ message: "error" }), {
        status: 500,
      });
    }

    const data = await response.json();

    if (!data) {
      return new Response(JSON.stringify({ message: "error" }), {
        status: 500,
      });
    }

    if (data.message === "invalid") {
      return new Response(JSON.stringify({ message: "invalid" }), {
        status: 200,
      });
    } else if (data.message === "completed") {
      return new Response(JSON.stringify({ message: "completed", user: data.user }), {
        status: 200,
      });
    } else {
      return new Response(JSON.stringify({ message: "valid" }), {
        status: 200,
      });
    }

  } catch (err) {
    console.log(err);
    return new Response(JSON.stringify({ message: "error" }), { status: 500 });
  }
}
