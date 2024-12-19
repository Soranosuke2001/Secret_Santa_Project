import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  try {
    const username = request.nextUrl.searchParams.get("username");

    const response = await fetch(
      `${process.env.BACKEND_ROLL_USERNAME}?username=${username}`
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

    if (data.message === "completed") {
      return new Response(JSON.stringify({ message: data.message, user: data.user }), {
        status: 200,
      });
    }

    return new Response(JSON.stringify({ message: data.message }), {
      status: 200,
    });
  } catch (err) {
    console.log(err);
    return new Response(JSON.stringify({ message: "error" }), { status: 500 });
  }
}
