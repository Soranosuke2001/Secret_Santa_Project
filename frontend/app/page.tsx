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
  const [usernameError, setUsernameError] = useState<boolean>(false);
  const [rollCompleted, setRollCompleted] = useState<boolean>(false);

  function clickHandler() {
    if (username === "") {
      setUsernameError(true);
      toast.error("名前が間違ってます")
      return;
    }

    // send request to backend to check username
    fetch(`${process.env.NEXT_PUBLIC_CHECK_USERNAME}?username=${username}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.message === "invalid") {
          setUsernameError(true);
        } else if (data.message === "completed") {
          setRollCompleted(true);
        } else {
          setRollCompleted(false);
          setUsernameError(false);
        }
      })
      .catch((e) => {
        console.log(e)
        toast.error("エラーが発生しました")
        toast.error(e)
      });

    if (usernameError) {
      toast.error("名前が間違ってます")
      return;
    }

    if (rollCompleted) {
      toast.error("違う名前を入力してね")
      return;
    }

    // get random name
    fetch(`${process.env.NEXT_PUBLIC_ROLL_USERNAME}?username=${username}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.message === "error") {
          toast.error("エラーが発生しました")
        }
        router.push(`/roll?username=${data.message}`);
      })
      .catch((e) => {
        console.log(e)
        toast.error("エラーが発生しました")
        toast.error(e)
      })
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
