"use client";

import { Button } from "@/components/ui/button";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Suspense, useState } from "react";
import { PiHandTapThin } from "react-icons/pi";

function Roll() {
  const searchParams = useSearchParams();
  const username = searchParams.get("username");

  // State to track card flipping
  const [isFlipped, setIsFlipped] = useState(false);

  // Toggle card flip state
  const handleCardClick = () => {
    setIsFlipped((prevState) => !prevState);
  };

  return (
    <section className="py-16 mx-auto">
      <div className="mx-auto flex justify-center object-center px-4 py-16">
        <div className="flex justify-center object-center flex-col gap-12">
          <h2 className="text-3xl font-semibold tracking-tight text-white mx-5">
            誰があったかな？？
          </h2>
          <div className="mx-auto grid gap-12 space-y-10">
            <div
              className="h-96 w-96 relative [perspective:1000px]" // Card container
              onClick={handleCardClick} // Handle clicks
              tabIndex={0} // Make card focusable
              role="button" // Semantic button role
              onKeyDown={(e) => {
                if (e.key === "Enter" || e.key === " ") {
                  handleCardClick(); // Flip on Enter or Space key
                }
              }}
            >
              <div
                className={`relative h-full w-full rounded-xl shadow-xl transition-transform duration-500 [transform-style:preserve-3d] ${
                  isFlipped ? "[transform:rotateY(180deg)]" : ""
                }`}
              >
                {/* Front face */}
                <div className="absolute inset-0 h-full w-full rounded-xl [backface-visibility:hidden] bg-neutral-900">
                  <div className="w-full mt-9">
                    <PiHandTapThin className="h-52 w-52 text-white mx-auto" />
                  </div>
                  <p className="text-2xl text-white text-center mt-9">
                    タップしてね
                  </p>
                </div>
                {/* Back face */}
                <div className="absolute inset-0 h-full w-full rounded-xl bg-neutral-900 px-12 text-center text-slate-200 [transform:rotateY(180deg)] [backface-visibility:hidden]">
                  <div className="flex min-h-full flex-col items-center justify-center">
                    <p className="text-5xl text-pretty text-center mb-4 text-white">
                      {username}
                    </p>
                    <p className="text-md text-pretty text-center mt-16 text-white">
                      {username} のためにプレゼント考えてね ^_^
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="text-right mr-10">
            <Link href="/">
              <Button className="text-lg p-6">Home</Button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Page() {
  return (
    <Suspense>
      <Roll />
    </Suspense>
  );
}
