<template>
  <div
    class="border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between"
  >
    <h3 class="text-2xl font-semibold leading-6 text-gray-900">예약</h3>
    <div class="mt-3 sm:ml-4 sm:mt-0">
      <button
        type="button"
        class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        추가하기
      </button>
    </div>
  </div>

  <div class="mt-5 grid grid-cols-2 divide-x divide-gray-200">
    <div class="pr-14">
      <div class="flex items-center">
        <!-- 현재 달력 -->
        <h2 class="flex-auto text-lg font-semibold text-gray-900">
          {{ current_year }}년 {{ current_month + 1 }}월
        </h2>

        <!-- 이전 달 -->
        <button
          type="button"
          class="-my-1.5 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
          @click="movePrevMonth"
        >
          <span class="sr-only">Previous month</span>
          <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
        </button>

        <!-- 다음 달 -->
        <button
          type="button"
          class="-my-1.5 -mr-1.5 ml-2 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
          @click="moveNextMonth"
        >
          <span class="sr-only">Next month</span>
          <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
        </button>
      </div>

      <!-- 요일 -->
      <div
        class="mt-10 grid grid-cols-7 text-center text-sm leading-6 text-black"
      >
        <div>월</div>
        <div>화</div>
        <div>수</div>
        <div>목</div>
        <div>금</div>
        <div class="text-blue-500">토</div>
        <div class="text-red-500">일</div>
      </div>

      <!-- 날짜 -->
      <div class="mt-2 grid grid-cols-7 text-sm">
        <div
          v-for="(day, dayIdx) in days"
          :key="day.date"
          :class="[dayIdx > 6 && 'border-t border-gray-200', 'py-2']"
        >
          <button
            type="button"
            :class="[
              day.isSelected && 'text-white',
              !day.isSelected && day.isToday && 'text-indigo-600',
              !day.isSelected &&
                !day.isToday &&
                day.isCurrentMonth &&
                'text-gray-900',
              !day.isSelected &&
                !day.isToday &&
                !day.isCurrentMonth &&
                'text-gray-400',
              day.isSelected && day.isToday && 'bg-indigo-600',
              day.isSelected && !day.isToday && 'bg-gray-900',
              !day.isSelected && 'hover:bg-gray-200',
              (day.isSelected || day.isToday) && 'font-semibold',
              'mx-auto flex h-8 w-8 items-center justify-center rounded-full',
            ]"
          >
            <time :datetime="day.date">{{
              day.date.split('-').pop().replace(/^0/, '')
            }}</time>
          </button>
        </div>
      </div>
    </div>

    <!-- 예약 목록 섹션 -->
    <section class="mt-0 pl-14">
      <!-- 선택된 날짜 -->
      <h2 class="text-lg font-semibold leading-6 text-gray-900">
        0000년 0월 0일
      </h2>

      <!-- 예약 목록 -->
      <ol class="mt-4 space-y-1 text-sm leading-6 text-gray-500">
        <li
          v-for="meeting in meetings"
          :key="meeting.id"
          class="group flex items-center space-x-4 rounded-xl px-4 py-2 focus-within:bg-gray-100 hover:bg-gray-100"
        >
          <div class="flex-auto">
            <p class="text-gray-900">{{ meeting.name }}</p>
            <p class="mt-0.5">
              <time :datetime="meeting.startDatetime">{{ meeting.start }}</time>
            </p>
          </div>

          <Menu
            as="div"
            class="relative opacity-0 focus-within:opacity-100 group-hover:opacity-100"
          >
            <div>
              <MenuButton
                class="-m-2 flex items-center rounded-full p-1.5 text-gray-500 hover:text-gray-600"
              >
                <span class="sr-only">Open options</span>
                <EllipsisVerticalIcon class="h-6 w-6" aria-hidden="true" />
              </MenuButton>
            </div>

            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <MenuItems
                class="absolute right-0 z-10 mt-2 w-36 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
              >
                <div class="py-1">
                  <MenuItem v-slot="{ active }">
                    <a
                      href="#"
                      :class="[
                        active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                        'block px-4 py-2 text-sm',
                      ]"
                      >Edit</a
                    >
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <a
                      href="#"
                      :class="[
                        active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                        'block px-4 py-2 text-sm',
                      ]"
                      >Cancel</a
                    >
                  </MenuItem>
                </div>
              </MenuItems>
            </transition>
          </Menu>
        </li>
      </ol>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/20/solid';
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { EllipsisVerticalIcon } from '@heroicons/vue/24/outline';
import { ref } from 'vue';

let days = ref([]);
let current_month = ref(0);
let current_year = ref(0);
let selected_date = ref(0);

const offset = new Date().getTimezoneOffset() * 60000;

const today = new Date(Date.now());
current_year.value = today.getFullYear();
current_month.value = today.getMonth();
selected_date.value = today.getDate();

let start_day_of_calendar = new Date(Date.now());
start_day_of_calendar.setDate(
  start_day_of_calendar.getDate() - start_day_of_calendar.getDay()
);

const calculateCalendar = (start_day_of_calendar: Date) => {
  const days = [];
  for (let i = 0; i < 42; i++) {
    let date = new Date(
      start_day_of_calendar.getFullYear(),
      start_day_of_calendar.getMonth(),
      start_day_of_calendar.getDate() + i
    );
    date = new Date(date.getTime() - offset);

    let cal_today =
      today.getFullYear() === date.getFullYear() &&
      today.getMonth() === date.getMonth() &&
      today.getDate() === date.getDate();

    let cal_current_month =
      current_year.value === date.getFullYear() &&
      current_month.value === date.getMonth();

    days.push({
      date: date.toISOString().split('T')[0],
      isToday: cal_today,
      isCurrentMonth: cal_current_month,
      isSelected: cal_today,
    });
  }

  return days;
};
days.value = calculateCalendar(start_day_of_calendar);

const movePrevMonth = () => {
  if (current_month.value === 0) {
    current_year.value = current_year.value - 1;
    current_month.value = 11;
  } else {
    current_month.value = current_month.value - 1;
  }

  start_day_of_calendar = new Date(current_year.value, current_month.value, 1);
  start_day_of_calendar.setDate(
    start_day_of_calendar.getDate() - start_day_of_calendar.getDay()
  );
  days.value = calculateCalendar(start_day_of_calendar);
};

const moveNextMonth = () => {
  if (current_month.value === 11) {
    current_year.value = current_year.value + 1;
    current_month.value = 0;
  } else {
    current_month.value = current_month.value + 1;
  }

  start_day_of_calendar = new Date(current_year.value, current_month.value, 1);
  start_day_of_calendar.setDate(
    start_day_of_calendar.getDate() - start_day_of_calendar.getDay()
  );
  days.value = calculateCalendar(start_day_of_calendar);
};

// const days = [
//   { date: '2021-12-27' },
//   { date: '2021-12-28' },
//   { date: '2021-12-29' },
//   { date: '2021-12-30' },
//   { date: '2021-12-31' },
//   { date: '2022-01-01', isCurrentMonth: true },
//   { date: '2022-01-02', isCurrentMonth: true },
//   { date: '2022-01-03', isCurrentMonth: true },
//   { date: '2022-01-04', isCurrentMonth: true },
//   { date: '2022-01-05', isCurrentMonth: true },
//   { date: '2022-01-06', isCurrentMonth: true },
//   { date: '2022-01-07', isCurrentMonth: true },
//   { date: '2022-01-08', isCurrentMonth: true },
//   { date: '2022-01-09', isCurrentMonth: true },
//   { date: '2022-01-10', isCurrentMonth: true },
//   { date: '2022-01-11', isCurrentMonth: true },
//   { date: '2022-01-12', isCurrentMonth: true, isToday: true },
//   { date: '2022-01-13', isCurrentMonth: true },
//   { date: '2022-01-14', isCurrentMonth: true },
//   { date: '2022-01-15', isCurrentMonth: true },
//   { date: '2022-01-16', isCurrentMonth: true },
//   { date: '2022-01-17', isCurrentMonth: true },
//   { date: '2022-01-18', isCurrentMonth: true },
//   { date: '2022-01-19', isCurrentMonth: true },
//   { date: '2022-01-20', isCurrentMonth: true },
//   { date: '2022-01-21', isCurrentMonth: true, isSelected: true },
//   { date: '2022-01-22', isCurrentMonth: true },
//   { date: '2022-01-23', isCurrentMonth: true },
//   { date: '2022-01-24', isCurrentMonth: true },
//   { date: '2022-01-25', isCurrentMonth: true },
//   { date: '2022-01-26', isCurrentMonth: true },
//   { date: '2022-01-27', isCurrentMonth: true },
//   { date: '2022-01-28', isCurrentMonth: true },
//   { date: '2022-01-29', isCurrentMonth: true },
//   { date: '2022-01-30', isCurrentMonth: true },
//   { date: '2022-01-31', isCurrentMonth: true },
//   { date: '2022-02-01' },
//   { date: '2022-02-02' },
//   { date: '2022-02-03' },
//   { date: '2022-02-04' },
//   { date: '2022-02-05' },
//   { date: '2022-02-06' },
// ];
const meetings = [
  {
    id: 1,
    name: 'Leslie Alexander',
    imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    start: '1:00 PM',
    startDatetime: '2022-01-21T13:00',
    end: '2:30 PM',
    endDatetime: '2022-01-21T14:30',
  },
  // More meetings...
];
</script>

<style scoped></style>
