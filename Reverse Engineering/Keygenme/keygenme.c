#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

int main()
{
    size_t sVar1;
    int uVar2;
    long in_FS_OFFSET;
    int local_d0;
    int local_cc;
    int local_c8;
    int local_c4;
    int local_c0;
    int local_ba;
    char local_b8[16];
    char local_a8[16];
    long local_98;
    long local_90;
    long local_88;
    long local_80;
    char local_78[12];
    char local_6c; // local_78[12]
    char local_66; // local_78[18]
    char local_5f; // local_78[25]
    char local_5e; // local_78[26]
    char local_58[32];
    char acStack56[40];
    long local_10;

    local_10 = *(long *)(in_FS_OFFSET + 0x28);
    local_98 = 0x7b4654436f636970; // picoCTF{
    local_90 = 0x30795f676e317262; // br1ng_y0
    local_88 = 0x6b5f6e77305f7275; // ur_0wn_k
    local_80 = 0x5f7933;           // 3y_
    local_ba = 0x7d;               // }

    sVar1 = strlen((char *)&local_98);
    MD5((uchar *)&local_98, sVar1, local_b8); // md5 hash into local_b8
    // local_b8 = 438218d572e90162d0981cbbc7d43882
    sVar1 = strlen((char *)&local_ba);
    MD5((uchar *)&local_ba, sVar1, local_a8);
    // local_a8 = cbb184dd8e05c9709e5dcaedaa0495cf
    local_d0 = 0;
    for (local_cc = 0; local_cc < 0x10; local_cc = local_cc + 1)
    {
        sprintf(local_78 + local_d0, "%02x", (ulong)local_b8[local_cc]);
        local_d0 = local_d0 + 2;
    }
    local_d0 = 0;
    for (local_c8 = 0; local_c8 < 0x10; local_c8 = local_c8 + 1)
    {
        sprintf(local_58 + local_d0, "%02x", (ulong)local_a8[local_c8]);
        local_d0 = local_d0 + 2;
    }
    for (local_c4 = 0; local_c4 < 0x1b; local_c4 = local_c4 + 1) // first 27 characters
    {
        acStack56[local_c4] = *(char *)((long)&local_98 + (long)local_c4);
    }

    // characters 27-35
    acStack56[27] = local_66;
    acStack56[28] = local_5e;
    acStack56[29] = local_5f;
    acStack56[30] = local_78[0];
    acStack56[31] = local_5e;
    acStack56[32] = local_66;
    acStack56[33] = local_6c;
    acStack56[34] = local_5e;
    acStack56[35] = local_ba; //}

    // the rest of the code compares acStack56 to your input key and returns 1 if it matches (valid)
    return;
}