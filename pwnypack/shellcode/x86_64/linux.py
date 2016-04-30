from pwnypack.shellcode.stack_data import stack_data_finalizer
from pwnypack.shellcode.x86.mutable_data import nasm_mutable_data_finalizer, nasm_null_safe_mutable_data_finalizer
from pwnypack.shellcode.x86_64.null_safe import X86_64NullSafe
from pwnypack.shellcode.types import NUMERIC, PTR, SyscallDef
from pwnypack.shellcode.linux import Linux
from pwnypack.shellcode.x86_64 import X86_64
from pwnypack.shellcode.x86_64.stack_data import x86_64_null_safe_stack_data_finalizer


__all__ = ['LinuxX86_64Mutable', 'LinuxX86_64MutableNullSafe', 'LinuxX86_64Stack', 'LinuxX86_64StackNullSafe']


class LinuxX86_64(Linux, X86_64):
    """
    An environment that targets a generic Linux X86_64 machine.
    """

    sys_rt_sigreturn = SyscallDef('sys_rt_sigreturn')  #:
    sys_modify_ldt = SyscallDef('sys_modify_ldt', NUMERIC, PTR, NUMERIC)  #:
    sys_arch_prctl = SyscallDef('sys_arch_prctl', NUMERIC, NUMERIC)  #:
    sys_iopl = SyscallDef('sys_iopl', NUMERIC)  #:
    sys_mmap = SyscallDef('sys_mmap', PTR, NUMERIC, NUMERIC, NUMERIC, NUMERIC, NUMERIC)  #:

    SYSCALL_REG = X86_64.RAX
    SYSCALL_ARG_MAP = [X86_64.RDI, X86_64.RSI, X86_64.RDX, X86_64.R10, X86_64.R8, X86_64.R9]
    SYSCALL_RET_REG = X86_64.RAX
    SYSCALL_INSTR = 'syscall'
    SYSCALL_MAP = {
        Linux.sys_read: 0,
        Linux.sys_write: 1,
        Linux.sys_open: 2,
        Linux.sys_close: 3,
        Linux.sys_newstat: 4,
        Linux.sys_newfstat: 5,
        Linux.sys_newlstat: 6,
        Linux.sys_poll: 7,
        Linux.sys_lseek: 8,
        sys_mmap: 9,
        Linux.sys_mprotect: 10,
        Linux.sys_munmap: 11,
        Linux.sys_brk: 12,
        Linux.sys_rt_sigaction: 13,
        Linux.sys_rt_sigprocmask: 14,
        sys_rt_sigreturn: 15,
        Linux.sys_ioctl: 16,
        Linux.sys_pread64: 17,
        Linux.sys_pwrite64: 18,
        Linux.sys_readv: 19,
        Linux.sys_writev: 20,
        Linux.sys_access: 21,
        Linux.sys_pipe: 22,
        Linux.sys_select: 23,
        Linux.sys_sched_yield: 24,
        Linux.sys_mremap: 25,
        Linux.sys_msync: 26,
        Linux.sys_mincore: 27,
        Linux.sys_madvise: 28,
        Linux.sys_shmget: 29,
        Linux.sys_shmat: 30,
        Linux.sys_shmctl: 31,
        Linux.sys_dup: 32,
        Linux.sys_dup2: 33,
        Linux.sys_pause: 34,
        Linux.sys_nanosleep: 35,
        Linux.sys_getitimer: 36,
        Linux.sys_alarm: 37,
        Linux.sys_setitimer: 38,
        Linux.sys_getpid: 39,
        Linux.sys_sendfile64: 40,
        Linux.sys_socket: 41,
        Linux.sys_connect: 42,
        Linux.sys_accept: 43,
        Linux.sys_sendto: 44,
        Linux.sys_recvfrom: 45,
        Linux.sys_sendmsg: 46,
        Linux.sys_recvmsg: 47,
        Linux.sys_shutdown: 48,
        Linux.sys_bind: 49,
        Linux.sys_listen: 50,
        Linux.sys_getsockname: 51,
        Linux.sys_getpeername: 52,
        Linux.sys_socketpair: 53,
        Linux.sys_setsockopt: 54,
        Linux.sys_getsockopt: 55,
        Linux.sys_clone: 56,
        Linux.sys_fork: 57,
        Linux.sys_vfork: 58,
        Linux.sys_execve: 59,
        Linux.sys_exit: 60,
        Linux.sys_wait4: 61,
        Linux.sys_kill: 62,
        Linux.sys_newuname: 63,
        Linux.sys_semget: 64,
        Linux.sys_semop: 65,
        Linux.sys_semctl: 66,
        Linux.sys_shmdt: 67,
        Linux.sys_msgget: 68,
        Linux.sys_msgsnd: 69,
        Linux.sys_msgrcv: 70,
        Linux.sys_msgctl: 71,
        Linux.sys_fcntl: 72,
        Linux.sys_flock: 73,
        Linux.sys_fsync: 74,
        Linux.sys_fdatasync: 75,
        Linux.sys_truncate: 76,
        Linux.sys_ftruncate: 77,
        Linux.sys_getdents: 78,
        Linux.sys_getcwd: 79,
        Linux.sys_chdir: 80,
        Linux.sys_fchdir: 81,
        Linux.sys_rename: 82,
        Linux.sys_mkdir: 83,
        Linux.sys_rmdir: 84,
        Linux.sys_creat: 85,
        Linux.sys_link: 86,
        Linux.sys_unlink: 87,
        Linux.sys_symlink: 88,
        Linux.sys_readlink: 89,
        Linux.sys_chmod: 90,
        Linux.sys_fchmod: 91,
        Linux.sys_chown: 92,
        Linux.sys_fchown: 93,
        Linux.sys_lchown: 94,
        Linux.sys_umask: 95,
        Linux.sys_gettimeofday: 96,
        Linux.sys_getrlimit: 97,
        Linux.sys_getrusage: 98,
        Linux.sys_sysinfo: 99,
        Linux.sys_times: 100,
        Linux.sys_ptrace: 101,
        Linux.sys_getuid: 102,
        Linux.sys_syslog: 103,
        Linux.sys_getgid: 104,
        Linux.sys_setuid: 105,
        Linux.sys_setgid: 106,
        Linux.sys_geteuid: 107,
        Linux.sys_getegid: 108,
        Linux.sys_setpgid: 109,
        Linux.sys_getppid: 110,
        Linux.sys_getpgrp: 111,
        Linux.sys_setsid: 112,
        Linux.sys_setreuid: 113,
        Linux.sys_setregid: 114,
        Linux.sys_getgroups: 115,
        Linux.sys_setgroups: 116,
        Linux.sys_setresuid: 117,
        Linux.sys_getresuid: 118,
        Linux.sys_setresgid: 119,
        Linux.sys_getresgid: 120,
        Linux.sys_getpgid: 121,
        Linux.sys_setfsuid: 122,
        Linux.sys_setfsgid: 123,
        Linux.sys_getsid: 124,
        Linux.sys_capget: 125,
        Linux.sys_capset: 126,
        Linux.sys_rt_sigpending: 127,
        Linux.sys_rt_sigtimedwait: 128,
        Linux.sys_rt_sigqueueinfo: 129,
        Linux.sys_rt_sigsuspend: 130,
        Linux.sys_sigaltstack: 131,
        Linux.sys_utime: 132,
        Linux.sys_mknod: 133,
        Linux.sys_personality: 135,
        Linux.sys_ustat: 136,
        Linux.sys_statfs: 137,
        Linux.sys_fstatfs: 138,
        Linux.sys_sysfs: 139,
        Linux.sys_getpriority: 140,
        Linux.sys_setpriority: 141,
        Linux.sys_sched_setparam: 142,
        Linux.sys_sched_getparam: 143,
        Linux.sys_sched_setscheduler: 144,
        Linux.sys_sched_getscheduler: 145,
        Linux.sys_sched_get_priority_max: 146,
        Linux.sys_sched_get_priority_min: 147,
        Linux.sys_sched_rr_get_interval: 148,
        Linux.sys_mlock: 149,
        Linux.sys_munlock: 150,
        Linux.sys_mlockall: 151,
        Linux.sys_munlockall: 152,
        Linux.sys_vhangup: 153,
        sys_modify_ldt: 154,
        Linux.sys_pivot_root: 155,
        Linux.sys_sysctl: 156,
        Linux.sys_prctl: 157,
        sys_arch_prctl: 158,
        Linux.sys_adjtimex: 159,
        Linux.sys_setrlimit: 160,
        Linux.sys_chroot: 161,
        Linux.sys_sync: 162,
        Linux.sys_acct: 163,
        Linux.sys_settimeofday: 164,
        Linux.sys_mount: 165,
        Linux.sys_umount2: 166,
        Linux.sys_swapon: 167,
        Linux.sys_swapoff: 168,
        Linux.sys_reboot: 169,
        Linux.sys_sethostname: 170,
        Linux.sys_setdomainname: 171,
        sys_iopl: 172,
        Linux.sys_ioperm: 173,
        Linux.sys_init_module: 175,
        Linux.sys_delete_module: 176,
        Linux.sys_quotactl: 179,
        Linux.sys_gettid: 186,
        Linux.sys_readahead: 187,
        Linux.sys_setxattr: 188,
        Linux.sys_lsetxattr: 189,
        Linux.sys_fsetxattr: 190,
        Linux.sys_getxattr: 191,
        Linux.sys_lgetxattr: 192,
        Linux.sys_fgetxattr: 193,
        Linux.sys_listxattr: 194,
        Linux.sys_llistxattr: 195,
        Linux.sys_flistxattr: 196,
        Linux.sys_removexattr: 197,
        Linux.sys_lremovexattr: 198,
        Linux.sys_fremovexattr: 199,
        Linux.sys_tkill: 200,
        Linux.sys_time: 201,
        Linux.sys_futex: 202,
        Linux.sys_sched_setaffinity: 203,
        Linux.sys_sched_getaffinity: 204,
        Linux.sys_io_setup: 206,
        Linux.sys_io_destroy: 207,
        Linux.sys_io_getevents: 208,
        Linux.sys_io_submit: 209,
        Linux.sys_io_cancel: 210,
        Linux.sys_lookup_dcookie: 212,
        Linux.sys_epoll_create: 213,
        Linux.sys_remap_file_pages: 216,
        Linux.sys_getdents64: 217,
        Linux.sys_set_tid_address: 218,
        Linux.sys_restart_syscall: 219,
        Linux.sys_semtimedop: 220,
        Linux.sys_fadvise64: 221,
        Linux.sys_timer_create: 222,
        Linux.sys_timer_settime: 223,
        Linux.sys_timer_gettime: 224,
        Linux.sys_timer_getoverrun: 225,
        Linux.sys_timer_delete: 226,
        Linux.sys_clock_settime: 227,
        Linux.sys_clock_gettime: 228,
        Linux.sys_clock_getres: 229,
        Linux.sys_clock_nanosleep: 230,
        Linux.sys_exit_group: 231,
        Linux.sys_epoll_wait: 232,
        Linux.sys_epoll_ctl: 233,
        Linux.sys_tgkill: 234,
        Linux.sys_utimes: 235,
        Linux.sys_mbind: 237,
        Linux.sys_set_mempolicy: 238,
        Linux.sys_get_mempolicy: 239,
        Linux.sys_mq_open: 240,
        Linux.sys_mq_unlink: 241,
        Linux.sys_mq_timedsend: 242,
        Linux.sys_mq_timedreceive: 243,
        Linux.sys_mq_notify: 244,
        Linux.sys_mq_getsetattr: 245,
        Linux.sys_kexec_load: 246,
        Linux.sys_waitid: 247,
        Linux.sys_add_key: 248,
        Linux.sys_request_key: 249,
        Linux.sys_keyctl: 250,
        Linux.sys_ioprio_set: 251,
        Linux.sys_ioprio_get: 252,
        Linux.sys_inotify_init: 253,
        Linux.sys_inotify_add_watch: 254,
        Linux.sys_inotify_rm_watch: 255,
        Linux.sys_migrate_pages: 256,
        Linux.sys_openat: 257,
        Linux.sys_mkdirat: 258,
        Linux.sys_mknodat: 259,
        Linux.sys_fchownat: 260,
        Linux.sys_futimesat: 261,
        Linux.sys_newfstatat: 262,
        Linux.sys_unlinkat: 263,
        Linux.sys_renameat: 264,
        Linux.sys_linkat: 265,
        Linux.sys_symlinkat: 266,
        Linux.sys_readlinkat: 267,
        Linux.sys_fchmodat: 268,
        Linux.sys_faccessat: 269,
        Linux.sys_pselect6: 270,
        Linux.sys_ppoll: 271,
        Linux.sys_unshare: 272,
        Linux.sys_set_robust_list: 273,
        Linux.sys_get_robust_list: 274,
        Linux.sys_splice: 275,
        Linux.sys_tee: 276,
        Linux.sys_sync_file_range: 277,
        Linux.sys_vmsplice: 278,
        Linux.sys_move_pages: 279,
        Linux.sys_utimensat: 280,
        Linux.sys_epoll_pwait: 281,
        Linux.sys_signalfd: 282,
        Linux.sys_timerfd_create: 283,
        Linux.sys_eventfd: 284,
        Linux.sys_fallocate: 285,
        Linux.sys_timerfd_settime: 286,
        Linux.sys_timerfd_gettime: 287,
        Linux.sys_accept4: 288,
        Linux.sys_signalfd4: 289,
        Linux.sys_eventfd2: 290,
        Linux.sys_epoll_create1: 291,
        Linux.sys_dup3: 292,
        Linux.sys_pipe2: 293,
        Linux.sys_inotify_init1: 294,
        Linux.sys_preadv: 295,
        Linux.sys_pwritev: 296,
        Linux.sys_rt_tgsigqueueinfo: 297,
        Linux.sys_perf_event_open: 298,
        Linux.sys_recvmmsg: 299,
        Linux.sys_fanotify_init: 300,
        Linux.sys_fanotify_mark: 301,
        Linux.sys_prlimit64: 302,
        Linux.sys_name_to_handle_at: 303,
        Linux.sys_open_by_handle_at: 304,
        Linux.sys_clock_adjtime: 305,
        Linux.sys_syncfs: 306,
        Linux.sys_sendmmsg: 307,
        Linux.sys_setns: 308,
        Linux.sys_getcpu: 309,
        Linux.sys_process_vm_readv: 310,
        Linux.sys_process_vm_writev: 311,
        Linux.sys_kcmp: 312,
        Linux.sys_finit_module: 313,
        Linux.sys_sched_setattr: 314,
        Linux.sys_sched_getattr: 315,
        Linux.sys_renameat2: 316,
        Linux.sys_seccomp: 317,
        Linux.sys_getrandom: 318,
        Linux.sys_memfd_create: 319,
        Linux.sys_kexec_file_load: 320,
        Linux.sys_bpf: 321,
        Linux.sys_execveat: 322,
        Linux.sys_userfaultfd: 323,
        Linux.sys_membarrier: 324,
        Linux.sys_mlock2: 325,
        Linux.sys_copy_file_range: 326,
    }


class LinuxX86_64Mutable(LinuxX86_64):
    """
    An environment that targets a 64-bit Linux X86 machine in a writable segment.
    """

    data_finalizer = nasm_mutable_data_finalizer


class LinuxX86_64MutableNullSafe(X86_64NullSafe, LinuxX86_64):
    """
    An environment that targets a 64-bit Linux X86 machine in a writable segment
    that emits no NUL bytes or carriage return characters.
    """

    data_finalizer = nasm_null_safe_mutable_data_finalizer


class LinuxX86_64Stack(LinuxX86_64):
    """
    An environment that targets a 64-bit Linux X86 machine that allocates
    the required data on the stack.
    """

    data_finalizer = stack_data_finalizer(16)


class LinuxX86_64StackNullSafe(X86_64NullSafe, LinuxX86_64):
    """
    An environment that targets a 64-bit Linux X86 machine that allocates
    the required data on the stack and emits no NUL bytes or carriage return
    characters.
    """

    data_finalizer = x86_64_null_safe_stack_data_finalizer(16)
