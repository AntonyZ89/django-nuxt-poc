<template>
  <ul class="flex flex-col md:flex-row items-stretch md:items-center gap-y-3 md:gap-x-3">
    <NavbarItem to="/" :name="$t('page.home')" />
    <NavbarItem to="/discipline" :name="$t('page.discipline', 0)" />

    <PermissionRole role="COORDINATOR">
      <NavbarItem to="/user" :name="$t('page.user', 0)" />
    </PermissionRole>
  </ul>
</template>
