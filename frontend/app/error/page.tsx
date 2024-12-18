"use client";

import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Error() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)] bg-black">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <div>
          <h1 className="text-white">エラーが発生しました</h1>
        </div>
        <div>
          <Link href="/">
            <Button className="bg-green-500">ホームに戻る</Button>
          </Link>
        </div>
      </main>
    </div>
  );
}
