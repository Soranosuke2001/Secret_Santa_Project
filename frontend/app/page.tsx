"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { useState } from "react";
import toast from "react-hot-toast";
import { GrLinkNext } from "react-icons/gr";

export default function Home() {
  const router = useRouter();
  const [username, setUsername] = useState<string>("");

  async function clickHandler() {
    if (username === "") {
      toast.error("名前が間違ってます")
      return;
    }

    // send request to backend to check username
    try {
      const response1 = await fetch(`${process.env.NEXT_PUBLIC_CHECK_USERNAME}?username=${username}`)
      const data = await response1.json()

      if (data === "invalid") {
        toast.error("名前が間違ってます")
        return;
      }

      if (data === "completed") {
        toast.error("違う名前を入力してね")
        return;
      }

      // get random name
      const response2 = await fetch(`${process.env.NEXT_PUBLIC_ROLL_USERNAME}?username=${username}`)
      const result = await response2.json()
  
      if (result.message === "error") {
        toast.error("エラーが発生しました")
        return;
      }
      
      router.push(`/roll?username=${result.message}`);
    } catch (e) {
      console.log(e)
      toast.error("エラーが発生しました")
      toast.error(e)
    }
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <div className="flex">
          <Image src="/santa.png" alt="Santa" width={100} height={100} />
          <h1 className="text-center text-3xl font-bold text-white">
            シークレット
            <br />
            <span className="text-red-600">サンタ</span>
            <br />
            ゲーム！
          </h1>
        </div>
        <div className="items-center justify-center w-full">
          <Label htmlFor="username" className="text-neutral-400">
            ローマ字で名前を入力してね。
          </Label>
          <Input
            id="username"
            placeholder="Sora"
            className="text-white"
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="w-full text-right">
          <Button className="bg-green-500" onClick={clickHandler}>
            <GrLinkNext />
          </Button>
        </div>
      </main>
    </div>
  );
}
