#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/param.h>

#define SCRIPT_NAME "openurl.rb"

int main(int argc, char **argv) {
  char *cmd;
  char pwd[MAXPATHLEN + 1];

  getcwd(pwd, sizeof(pwd));

  cmd = malloc(sizeof(char) * (strlen(pwd) + 1 + strlen(SCRIPT_NAME) + 1));
  sprintf(cmd, "%s/%s", pwd, SCRIPT_NAME);

  execl(cmd, cmd, NULL);
  return 1;
}
