## **⚠️ GLIBC Compatibility Notice**

### **🔍 Check Your GLIBC Version**

Before running the precompiled binary, it is recommended to verify your system's installed GLIBC version:

```bash
ldd --version
```

You should see output similar to:

```
ldd (Debian GLIBC 2.41-6) 2.41
```

Ensure that your version is **2.38 or higher**. If it is, you may proceed to run the binary.

---

### **🛑 Common Error (Older GLIBC Versions)**

If your system does not meet the minimum GLIBC requirement, you may encounter an error such as:

```bash
/lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.38' not found
```

This indicates that the binary cannot execute due to an outdated version of the GNU C Library (GLIBC).

---

### **✅ Solution: Update Your System**

To resolve this issue, update your system using the appropriate command based on your Linux distribution:

#### Debian / Ubuntu / Kali / Linux Mint

```bash
sudo apt update && sudo apt upgrade
```

#### Arch / Manjaro

```bash
sudo pacman -Syu
```

#### Fedora

```bash
sudo dnf upgrade --refresh
```

#### openSUSE

```bash
sudo zypper refresh && sudo zypper update
```

#### Pop!\_OS

```bash
sudo apt update && sudo apt full-upgrade
```

---

### **🔁 Verify After Upgrading**

Once your system has been updated, re-run the following command to confirm that GLIBC 2.38 or newer is installed:

```bash
ldd --version
```

If the version is **2.38 or higher**, the precompiled binary should run without any issues.
